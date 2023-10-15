#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python List
 *
 * @p: a Python Object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list = (PyListObject *)(p);
	Py_ssize_t len, allocated;

	len = PyList_Size(p);
	allocated = list->allocated;
	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < len; i++)
		printf("Element %d: %s\n",
		       i, Py_TYPE(list->ob_item[i])->tp_name);
}
