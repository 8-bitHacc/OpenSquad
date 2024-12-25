#ifndef sss_RANDOMBYTES_H
#define sss_RANDOMBYTES_H

/*
 * Write `n` bytes of high quality random bytes to `buf`
 */
extern void randombytes(unsigned char *buf, long long n);

#endif /* sss_RANDOMBYTES_H */