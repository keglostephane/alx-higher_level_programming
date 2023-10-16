#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python bytes
 *
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	int i, j;
	const char *str;
	const char *type;
	Py_ssize_t len;

	type = p->ob_type->tp_name;

	printf("[.] bytes object info\n");

	if (strcmp(type, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		dprintf(STDERR_FILENO, "[ERROR]: Invalid Bytes Objects\n");
	}

	if (!strcmp(type, "bytes"))
	{
		len = PyBytes_Size(p);
		printf("  size: %zd\n", len);

		str = PyBytes_AsString(p);

		if (str)
			printf("  trying string: %s\n", str);
		if (len < 10)
			printf("  first %zd bytes: ", len + 1);
		else
			printf("  first %d bytes: ", 10);
		j = (len < 10) ? len + 1 : 10;
		for (i = 0; i < j - 1; i++)
			printf("%02x ", (unsigned char)(str[i]));
		printf("%02x\n", (unsigned char)(str[i]));
	}
}

/**
 * print_python_list - prints some basic info about Python lists
 *
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	int i;
	const char *type;
	PyListObject *list = (PyListObject *)(p);
	Py_ssize_t len;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < len; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
