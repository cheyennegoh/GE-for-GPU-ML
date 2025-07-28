#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

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

__global__
void evaluate0(float *x, float *pred)
{
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid >= 10) return;

	x += 2 * tid;
	pred += 10 * 0;

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

	pred[tid] = r[0];
}
__global__
void evaluate1(float *x, float *pred)
{
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid >= 10) return;

	x += 2 * tid;
	pred += 10 * 1;

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

	pred[tid] = r[0];
}
__global__
void evaluate2(float *x, float *pred)
{
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid >= 10) return;

	x += 2 * tid;
	pred += 10 * 2;

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

	pred[tid] = r[0];
}
__global__
void evaluate3(float *x, float *pred)
{
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid >= 10) return;

	x += 2 * tid;
	pred += 10 * 3;

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

	pred[tid] = r[0];
}
__global__
void evaluate4(float *x, float *pred)
{
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid >= 10) return;

	x += 2 * tid;
	pred += 10 * 4;

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

	pred[tid] = r[0];
}

int main(int argc, char *argv[])
{
	float *x, *pred, *d_x, *d_pred;

	x = (float *)malloc(10 * 2 * sizeof(float));
	pred = (float *)malloc(5 * 10 * sizeof(float));

	if (argc > 1)
	{
		read_data(argv[1], (float *)x, 10 * 2);
	}

	cudaMalloc(&d_x, 10 * 2 * sizeof(float));
	cudaMalloc(&d_pred, 5 * 10 * sizeof(float));

	cudaMemcpy(d_x, x, 10 * 2 * sizeof(float), cudaMemcpyHostToDevice);

	evaluate0<<<((10 + 255) / 256), 256>>>(d_x, d_pred);
	evaluate1<<<((10 + 255) / 256), 256>>>(d_x, d_pred);
	evaluate2<<<((10 + 255) / 256), 256>>>(d_x, d_pred);
	evaluate3<<<((10 + 255) / 256), 256>>>(d_x, d_pred);
	evaluate4<<<((10 + 255) / 256), 256>>>(d_x, d_pred);

	cudaMemcpy(pred, d_pred, 5 * 10 * sizeof(float), cudaMemcpyDeviceToHost);

	if (argc > 2)
	{
		write_data(argv[2], (float *)pred, 5 * 10);
	}

	cudaFree(d_x);
	cudaFree(d_pred);

	free(x);
	free(pred);

	return 0;
}
