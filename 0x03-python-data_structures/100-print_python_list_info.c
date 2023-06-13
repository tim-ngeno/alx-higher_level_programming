#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_list_info - print information about python lists
 * @p: python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p);
{
	int t;
	int size = 0;
	PyObject *m;
	PyListObject *n = ((PyListObject *) p);

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) n->allocated);

	for (t = 0; t < size; t++)
	{
		printf("Element %d: ", t);
		m = PyList_GetItem(p, t);
		printf("%s\n", Py_TYPE(m)->tp_name);
	}
}
