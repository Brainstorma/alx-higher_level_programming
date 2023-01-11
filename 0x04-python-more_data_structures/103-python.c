#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: void
 **/
void print_python_bytes(PyObject *p)
{
	char *string;
	long int sz, i, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sz = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  sz: %ld\n", sz);
	printf("  trying string: %s\n", string);

	if (sz >= 10)
		lmt = 10;
	else
		lmt = sz + 1;

	printf("  first %ld bytes:", lmt);

	for (i = 0; i < lmt; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: void
 **/
void print_python_list(PyObject *p)
{
	long int sz, i;
	PyListObject *list;
	PyObject *obj;

	sz = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] sz of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < sz; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
