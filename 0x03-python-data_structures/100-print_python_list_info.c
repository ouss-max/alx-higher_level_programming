#include <Python.h>
#include <object.h>
#include <listobject.h>

void display_python_list_info(PyObject *listObj)
{
    long int listSize = PyList_Size(listObj);
    int i;
    PyListObject *list = (PyListObject *)listObj;

    printf("[*] Size of the Python List = %li\n", listSize);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < listSize; i++)
        printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}