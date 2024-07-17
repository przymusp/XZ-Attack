///////////////////////////////////////////////////////////////////////////////
//
/// \file       test_vli_coder.c
/// \brief      Test VLI coder
//
//  Author:
//
//  This file has been put into the public domain.
//  You can do whatever you want with this file.
//
///////////////////////////////////////////////////////////////////////////////
#include "tests.h"
#include <time.h>
#include <stdlib.h>

//Test Single-call
static bool test_single_call(void)
{
    uint8_t out[LZMA_VLI_BYTES_MAX];
    size_t out_pos = 0;
    size_t out_size = LZMA_VLI_BYTES_MAX;

    uint64_t vli = rand();
    out_pos = 0;
    lzma_vli_encode(vli, NULL, out, &out_pos, out_size);

    uint64_t result;
    out_pos = 0;
    lzma_vli_decode(&result, NULL, out, &out_pos, out_size);

    if (vli != result)
        return false;

    return true;
}

//Test Multi-call
static bool test_multi_call(void)
{
    uint8_t tmp[LZMA_VLI_BYTES_MAX];
    static uint8_t n = 2;
    uint8_t out[n];
    size_t out_pos = 0;
    size_t vli_pos = 0;

    uint64_t vli = rand();
    uint8_t index = 0;
    lzma_ret res = LZMA_OK;
    while (res != LZMA_STREAM_END)
    {
        out_pos = 0;
        res = lzma_vli_encode(vli, &vli_pos, out, &out_pos, n);
        //storage
        for (int i = 0; i < out_pos; i++)
        {
            if (index > LZMA_VLI_BYTES_MAX)
                return false;
            tmp[index] = out[i];
            index++;
        }
    }
    uint8_t size = index + 1; //valid size of tmp

    uint64_t result_multi_call;
    vli_pos = 0;
    index = 0;
    res = LZMA_OK;
    while (res != LZMA_STREAM_END)
    {
        for (int i = 0; i < n; i++)
        {
            if (index < size)
            {
                if (index > LZMA_VLI_BYTES_MAX)
                    return false;
                out[i] = tmp[index];
            }
            else
            {
                out[i] = 0;
            }
            index++;
        }

        out_pos = 0;
        res = lzma_vli_decode(&result_multi_call, &vli_pos, out, &out_pos, n);
    }
    if (vli != result_multi_call)
        return false;

    uint64_t result_single_call;
    out_pos = 0;
    lzma_vli_decode(&result_single_call, NULL, tmp, &out_pos, size);
    if (vli != result_single_call)
        return false;

    return true;
}

int main(void)
{
    bool result = true;
    srand((unsigned)time(NULL));
    for (int i = 0; i < 10; i++)
    {
        result &= test_single_call();
        result &= test_multi_call();
    }
    return result ? 0 : 1;
}