#include <iostream>

typedef unsigned char byte;

void print_byte(byte p) {
    for (int i = 7; i >= 0; i--) {
        if ((1 << i) & p)
            printf("1");
        else
            printf("0");
    }
}

template<typename T, bool binary>
struct print {};

template<typename T>
struct print<T, true> {
    void operator() (T x) const {
        byte *p = (byte *)&x;

        for (int i = 0; i < sizeof(T) / sizeof(byte); i++) {
            print_byte(*p);
            printf(" ");
            p++;
        }
        printf("\n");
    }
};

template<typename T>
struct print<T, false> {
    void operator() (T x) const {
        byte *p = (byte *)&x;

        for (int i = 0; i < sizeof(T) / sizeof(byte); i++) {
            printf("%x ", *p);
            p++;
        }
        printf("\n");
    }
};


int main() {
    print<int, true>{}(0x12345678);
    print<int, false>{}(0x12345678);

    print<float, true>{}(123.456);
    print<float, false>{}(123.456);

    print<float, true>{}(-123.456);
    print<float, false>{}(-123.456);
    return 0;
}