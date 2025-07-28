#include <math.h>
#include <stdio.h>
#include <string.h>

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

	if (4 > 3)
	r[0] = sinf(r[0]);
	if (3 > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 8)
	r[0] = cosf(r[0]);
	if (4 > 9)
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > r[1])
	r[0] = cosf(r[0]);
	if (2 > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 5)
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (3 > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > 2)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (3 > 5)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > r[1])
	r[0] = cosf(r[0]);
	if (3 > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (3 > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > 1)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	if (r[1] > 3)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > 8)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 8)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > 3)
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > 2)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (3 > 7)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > 8)
	r[0] = sinf(r[0]);
	if (3 > x[0])
	r[0] = cosf(r[0]);
	if (1 > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	if (6 > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 4)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 5)
	r[0] = cosf(r[0]);
	if (x[1] > 8)
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (r[1] > 5)
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > r[0])
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (8 > 6)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > 3)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	if (5 > 8)
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (4 > 9)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 5)
	r[0] = cosf(r[0]);
	if (r[0] > 7)
	r[0] = sinf(r[0]);
	if (4 > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 8)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (1 > 9)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (8 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 6)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (8 > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > 2)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);
	if (2 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (7 > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > 2)
	r[0] = sinf(r[0]);
	if (9 > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > 6)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 6)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (1 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > 9)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	if (3 > 2)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > 8)
	r[0] = cosf(r[0]);
	if (4 > r[0])
	r[0] = cosf(r[0]);
	if (5 > 6)
	r[0] = sinf(r[0]);
	if (6 > 8)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > r[1])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	if (1 > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);

	return r[0];
}
float evaluate1(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (x[0] > 1)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > r[1])
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (9 > r[0])
	r[0] = sinf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > 8)
	r[0] = cosf(r[0]);
	if (r[1] > 5)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > 2)
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[1])
	r[0] = cosf(r[0]);
	if (r[0] > 3)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > 4)
	r[0] = sinf(r[0]);
	if (8 > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > 4)
	r[0] = cosf(r[0]);
	if (3 > 2)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	if (x[0] > 1)
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (5 > x[0])
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (x[1] > 6)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (4 > r[1])
	r[0] = sinf(r[0]);
	if (6 > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > 3)
	r[0] = sinf(r[0]);
	if (7 > 3)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (9 > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (3 > 7)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > 9)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 8)
	r[0] = cosf(r[0]);
	if (5 > x[0])
	r[0] = sinf(r[0]);
	if (6 > 8)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	if (3 > 8)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 4)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > 8)
	r[0] = sinf(r[0]);
	if (x[0] > 3)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 4)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (7 > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 5)
	r[0] = sinf(r[0]);
	if (4 > 2)
	r[0] = sinf(r[0]);
	if (x[0] > 1)
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (1 > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 5)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > 6)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[0] > 6)
	r[0] = sinf(r[0]);
	if (r[1] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 1)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 6)
	r[0] = sinf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 1)
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 6)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > x[0])
	r[0] = cosf(r[0]);
	if (r[0] > 2)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 5)
	r[0] = cosf(r[0]);
	if (9 > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	if (8 > x[0])
	r[0] = cosf(r[0]);
	if (7 > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > 9)
	r[0] = cosf(r[0]);
	if (1 > r[1])
	r[0] = sinf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > x[1])
	r[0] = sinf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > 4)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 1)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > 8)
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > 8)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (5 > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > 1)
	r[0] = cosf(r[0]);
	if (x[1] > 6)
	r[0] = cosf(r[0]);
	if (6 > 5)
	r[0] = cosf(r[0]);
	if (x[1] > 6)
	r[0] = sinf(r[0]);
	if (4 > r[0])
	r[0] = cosf(r[0]);

	return r[0];
}
float evaluate2(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	r[0] = sinf(r[0]);
	if (x[0] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 9)
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	if (3 > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 7)
	r[0] = cosf(r[0]);
	if (r[1] > 9)
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 1)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = sinf(r[0]);
	if (9 > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (4 > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 2)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (4 > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > 3)
	r[0] = sinf(r[0]);
	if (3 > 6)
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 2)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (3 > 4)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > 7)
	r[0] = cosf(r[0]);
	if (3 > x[1])
	r[0] = sinf(r[0]);
	if (4 > x[0])
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 1)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > 1)
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > 3)
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = cosf(r[0]);
	if (8 > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 4)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 3)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > 1)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 6)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 2)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > 5)
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > 1)
	r[0] = cosf(r[0]);
	if (9 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 9)
	r[0] = cosf(r[0]);
	if (r[0] > 1)
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > 5)
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = sinf(r[0]);
	if (1 > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > 8)
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > 3)
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (3 > r[0])
	r[0] = sinf(r[0]);
	if (r[1] > 5)
	r[0] = sinf(r[0]);
	if (r[1] > 7)
	r[0] = sinf(r[0]);
	if (8 > x[1])
	r[0] = cosf(r[0]);
	if (1 > 3)
	r[0] = cosf(r[0]);
	if (r[1] > 3)
	r[0] = cosf(r[0]);
	if (r[0] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 9)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > x[1])
	r[0] = sinf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > 1)
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > 3)
	r[0] = sinf(r[0]);
	if (1 > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (8 > 6)
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = cosf(r[0]);

	return r[0];
}
float evaluate3(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	r[0] = sinf(r[0]);
	if (x[0] > 5)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 3)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > r[0])
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (r[0] > 7)
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	if (4 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 6)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > 3)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 6)
	r[0] = cosf(r[0]);
	if (9 > r[0])
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 9)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > 5)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (1 > 7)
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (9 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (7 > 1)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 2)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > 5)
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (r[0] > 6)
	r[0] = sinf(r[0]);
	if (5 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > x[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (7 > 8)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > 4)
	r[0] = cosf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 3)
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 5)
	r[0] = sinf(r[0]);
	if (x[1] > 1)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 4)
	r[0] = cosf(r[0]);
	if (5 > r[0])
	r[0] = cosf(r[0]);
	if (7 > 9)
	r[0] = sinf(r[0]);
	if (r[0] > 7)
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 4)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 6)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (7 > 6)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (2 > 2)
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > 5)
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (x[0] > 2)
	r[0] = cosf(r[0]);
	if (4 > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 5)
	r[0] = sinf(r[0]);
	if (r[1] > 5)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > 8)
	r[0] = sinf(r[0]);
	if (x[1] > 7)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (4 > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > 7)
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	if (4 > r[1])
	r[0] = sinf(r[0]);
	if (x[1] > 7)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	if (9 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (6 > x[1])
	r[0] = cosf(r[0]);
	if (4 > 3)
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	if (5 > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (5 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > 8)
	r[0] = cosf(r[0]);
	if (r[0] > 6)
	r[0] = sinf(r[0]);
	if (3 > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);

	return r[0];
}
float evaluate4(float x[2])
{
	float r[2];

	for (int i = 0; i < 2; i++) r[i] = x[i % 2];

	if (x[0] > 6)
	r[0] = cosf(r[0]);
	if (2 > r[0])
	r[0] = sinf(r[0]);
	if (3 > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > 9)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 6)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > 9)
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (3 > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (9 > 3)
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (5 > 8)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 9)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 1)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 6)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (9 > x[1])
	r[0] = sinf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (5 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > 3)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > 2)
	r[0] = cosf(r[0]);
	if (2 > x[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 2)
	r[0] = sinf(r[0]);
	if (7 > x[0])
	r[0] = cosf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (5 > 1)
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 6)
	r[0] = sinf(r[0]);
	if (2 > 5)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (9 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > 1)
	r[0] = cosf(r[0]);
	if (3 > x[0])
	r[0] = sinf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (5 > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (1 > 8)
	r[0] = sinf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (1 > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = sinf(r[0]);
	if (6 > 9)
	r[0] = cosf(r[0]);
	if (r[1] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (5 > x[0])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (r[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > 7)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = sinf(r[0]);
	if (r[0] > 4)
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > r[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (6 > r[1])
	r[0] = cosf(r[0]);
	if (5 > x[0])
	r[0] = sinf(r[0]);
	if (8 > 7)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (5 > 5)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (6 > r[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > r[1])
	r[0] = cosf(r[0]);
	if (6 > x[0])
	r[0] = sinf(r[0]);
	if (r[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 1)
	r[0] = sinf(r[0]);
	if (3 > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (8 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[0])
	r[0] = cosf(r[0]);
	if (r[1] > 1)
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > 6)
	r[0] = sinf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (3 > 1)
	r[0] = cosf(r[0]);
	if (2 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (7 > 9)
	r[0] = cosf(r[0]);
	if (r[0] > r[0])
	r[0] = cosf(r[0]);
	if (r[1] > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 1)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	if (9 > r[0])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (2 > x[0])
	r[0] = sinf(r[0]);
	if (x[1] > x[1])
	r[0] = cosf(r[0]);
	if (x[1] > r[0])
	r[0] = cosf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (5 > r[1])
	r[0] = cosf(r[0]);
	if (7 > x[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (r[1] > x[1])
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (4 > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (r[0] > 8)
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > x[0])
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (r[1] > r[1])
	r[0] = cosf(r[0]);
	if (3 > r[1])
	r[0] = cosf(r[0]);
	if (r[0] > x[0])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[1] > r[1])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > x[1])
	r[0] = cosf(r[0]);
	r[0] = cosf(r[0]);
	if (8 > 4)
	r[0] = cosf(r[0]);
	if (x[0] > r[1])
	r[0] = cosf(r[0]);
	if (7 > 3)
	r[0] = sinf(r[0]);
	r[0] = cosf(r[0]);
	if (9 > 1)
	r[0] = cosf(r[0]);
	if (8 > r[0])
	r[0] = cosf(r[0]);
	r[0] = sinf(r[0]);
	r[0] = sinf(r[0]);
	if (x[0] > r[0])
	r[0] = cosf(r[0]);

	return r[0];
}

int main(int argc, char *argv[])
{
	static float x[10][2] = {{-3.3587572106361017, 3.3587572106361}, {-3.169977896903455, 2.1181115133872317}, {-0.7291859308382289, -1.09130386614709}, {-4.503912720992522, 1.8655817327798139}, {-2.604235467279385, 3.897513807668181}, {-4.734882604120344, -1.961252590871088}, {-1.4930950012401814, 2.23457458306309}, {2.9514668629166354, 4.417182315357273}, {-1.3872274423234532, 3.3490633053534133}, {-4.313248613819454, -2.882020583789186}};
	static float pred[5][10];

	for (int i = 0; i < 10; i++)
	{
		pred[0][i] = evaluate0(x[i]);
		pred[1][i] = evaluate1(x[i]);
		pred[2][i] = evaluate2(x[i]);
		pred[3][i] = evaluate3(x[i]);
		pred[4][i] = evaluate4(x[i]);
	}

	if (argc > 1)
	{
		write_data(argv[1], (float *)pred, 5 * 10);
	}

	return 0;
}
