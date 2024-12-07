console.log("hi from frida!");

function log(a) {
    var f = new File('/sdcard/scripts/logs.txt', 'a')
    f.write(a+"\n")
    f.close()
}

const base = Module.findBaseAddress("libg.so")

const libc = Process.findModuleByName('libc.so');

const free = new NativeFunction(libc.findExportByName('free'), 'void', ['pointer']);
const malloc = new NativeFunction(libc.findExportByName('malloc'), 'pointer', ['int']);
const androidWrite = new NativeFunction(Module.getExportByName(null, '__android_log_write'), 'int', ['int', 'pointer', 'pointer']);
const debugCtor = new NativeFunction(base.add(0x8AE8E4), "pointer", ["pointer"]);
const stageAddChild = new NativeFunction(base.add(0xA5C39C), "void", ["pointer", "pointer"]);
const debugMenuUpdate = new NativeFunction(base.add(0x5F5E58), "pointer", ["int", "float"])
const debugCtorAlloc = malloc(1000); // allocate memory

function patch(start, end) {
    Memory.patchCode(base.add(start), Process.pageSize, code => {
        const writer = new Arm64Writer(code);
        writer.putBImm(base.add(end));
        writer.flush();
    });
}

// To see debug logs, use: adb logcat | findstr "squadbust"
function debugLog(text){
    const tag = Memory.allocUtf8String("squadbust");
    const str = Memory.allocUtf8String(text);
    androidWrite(3, tag, str);
}

function patchRet(target) {
    Memory.patchCode(base.add(target), Process.pageSize, code => {
        const writer = new Arm64Writer(code);
        writer.putRet();
        writer.flush();
    });
}

Interceptor.replace(Module.findExportByName("libc.so", 'openat'), new NativeCallback(function() {
    return -1;
}, 'void', []));

patch(0x893E40, 0x894C00);
patch(0x862D70, 0x866784);
patch(0x79C210, 0x79CFD4);
patch(0x79D1CC, 0x79E13C);
patch(0x7C48C4, 0x7C56D0);
patch(0x395470, 0x396940);

Memory.protect(base.add(0x7C61EC), 4, 'rwx');
base.add(0x7C61EC).writeByteArray([8, 0, 128, 210]);

Memory.protect(base.add(0x7C61F4), 4, 'rwx');
base.add(0x7C61F4).writeByteArray([8, 0, 128, 210]);

patchRet(0x8760EC);
patchRet(0xA31C48);
patchRet(0x831108);
patchRet(0x71F878);
patchRet(0x71DE00);
patchRet(0x5F90C8);

Process.setExceptionHandler(function (details) {
    debugLog(details.type);
    debugLog(details.address.sub(base));
    debugLog(details.memory.address.sub(base));
    return false;
})

Interceptor.attach(libc.findExportByName("getaddrinfo"), {
    onEnter(args) {
        if (args[1].readUtf8String() == "9339") {
            args[0].writeUtf8String("127.0.0.1"); // Change your ip here
        }
    }
});

Interceptor.replace(base.add(0x7548d0), new NativeCallback(function(a1) {
    a1.writeByteArray([0xFF, 0x45, 0x12, 0x7A, 0x9C, 0x23, 0x4B, 0x67, 0xA1, 0x2D, 0x3E, 0x56, 0x90, 0xAB, 0xC8, 0xD3, 0xE5, 0xF4, 0x6B, 0x72, 0x85, 0x19, 0x3A, 0x4F, 0x28, 0x63, 0x92, 0xBD, 0xFA, 0x34, 0x76, 0x08]);
}, 'void', ['pointer']));

Interceptor.attach(base.add(0x9D300C), {
    onEnter(args) {
        debugLog(`[Debugger::WARNING] ${args[0].readUtf8String()}`);
    }
});

Interceptor.attach(base.add(0xAD8378), {
    onEnter(args) {
        debugLog(`[Debugger::ERROR] ${args[0].readUtf8String()}`);
    }
});
// 0x424C58 = LoadingScreen::update
const addDebug = Interceptor.attach(base.add(0x424C58), {
    onLeave(args) {
        debugLog("debug");
        debugCtor(debugCtorAlloc);
        stageAddChild(base.add(0x12E8D58).readPointer(), debugCtorAlloc);
        addDebug.detach();
    }
})

Interceptor.attach(libc.findExportByName("pthread_cond_signal"), {
	onEnter: function(args) {
		debugMenuUpdate(debugCtorAlloc, 0);
	}
});