/* Minimal main program -- everything is loaded from the library */

#include "Python.h"

#ifdef MS_WINDOWS
int
wmain(int argc, wchar_t **argv)
{
    return Py_Main(argc, argv);
}
#else
int
main(int argc, char **argv)
{
    putenv("PYTHONSTARTUP=/etc/python3/SCHET_DREVNIH_RUSOV.py");

    int a =  Py_BytesMain(argc, argv);

    printf("ШУЕ\n");

    return a;
}
#endif
