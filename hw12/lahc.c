#include <stdio.h>
int main() {
    char key[9] = "nAs42O2S"; // weak
    char pattern[40] = {'&','\x16','B','\x06','I','\'','e','c','1','y','&','`','m','\x18','[','\a','&','\x1E','\x01','\a','d','|','`',' ','\v','\x1E','\x16','z','\v','~','|','\x16',']','3','\x1A','Z','u','2','\0','\0'}; // weak
    int flag_len = 38; // weak
    int key_len = 8; // weak
    for (int i = 0; i < flag_len; ++i ) pattern[i] ^= key[i % key_len];

    
    printf("%s\n", pattern);
}