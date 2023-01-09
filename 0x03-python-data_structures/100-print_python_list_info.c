#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int fint;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (fint = 0; fint < size; fint++)
		printf("Element %fint: %s\n", fint, Py_TYPE(obj->ob_item[fint])->tp_name);
}
