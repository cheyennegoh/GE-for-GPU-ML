#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_data(char *filename, float *data, size_t size)
{
	FILE *file = fopen(filename, "rb");
	fread(data, sizeof(float), size, file);
	fclose(file);
}

void write_data(char *filename, float *data, size_t size)
{
	FILE *file = fopen(filename, "wb");
	fwrite(data, sizeof(float), size, file);
	fclose(file);
}

float evaluate0(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (x[1] > 8)
	r[0] = cosf(r[0]);

	return r[0];
}
float evaluate1(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (4 > 8)
	r[0] = cosf(r[0]);

	return r[0];
}
float evaluate2(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	r[0] = sinf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);

	return r[0];
}
float evaluate3(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (5 > x[1])
	r[0] = sinf(r[0]);
	if (6 > r[0])
	r[0] = sinf(r[0]);

	return r[0];
}
float evaluate4(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (3 > 4)
	r[0] = sinf(r[0]);

	return r[0];
}

int main(int argc, char *argv[])
{
	float *x, *pred;

	x = (float *)malloc(10 * 2 * sizeof(float));
	pred = (float *)malloc(5 * 10 * sizeof(float));

	if (argc > 1)
	{
		read_data(argv[1], (float *)x, 10 * 2);
	}

	for (int i = 0; i < 10; i++)
	{
		pred[10 * 0 + i] = evaluate0(&x[2 * i]);
		pred[10 * 1 + i] = evaluate1(&x[2 * i]);
		pred[10 * 2 + i] = evaluate2(&x[2 * i]);
		pred[10 * 3 + i] = evaluate3(&x[2 * i]);
		pred[10 * 4 + i] = evaluate4(&x[2 * i]);
	}

	if (argc > 2)
	{
		write_data(argv[2], (float *)pred, 5 * 10);
	}

	free(x);
	free(pred);

	return 0;
}
