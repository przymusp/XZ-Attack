///////////////////////////////////////////////////////////////////////////////
//
/// \file       test_vli_size.c
/// \brief      Test lzma_vli_size
//
//  Author:
//
//  This file has been put into the public domain.
//  You can do whatever you want with this file.
//
///////////////////////////////////////////////////////////////////////////////
#include "tests.h"

static uint64_t vli = UINT64_MAX / 2;
uint64_t vli_value;
static uint64_t vlis[9];
static uint32_t vlis_index[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
uint32_t vlis_index_value;

//generate value : 2^N - 1, N = {6, 13, 20, 27, 34, 41, 48, 55, 62}
static bool init_vlis(void)
{
    uint64_t j = 64;
    uint64_t k = 7;
    for (int i = 0; i < 9; i++)
    {
        j = j - k;
        vlis[i] = vli >> j;
        k += 7;
        j = 64;
    }
    return true;
}

//Test 1
static bool test_valid_vli_size(void)
{
    uint32_t result;

    for (int i = 0; i < 9; i++)
    {
        vli_value = vlis[i];
        vlis_index_value = vlis_index[i];
        result = lzma_vli_size(vli_value);
        if (vlis_index_value != result)
            return false;
    }
    return true;
}

//Test 2
static bool test_invalid_vli_size(void)
{
    uint32_t result;

    result = lzma_vli_size(vli + 1);
    if (result == 0)
        return true;
    return false;
}

int main(void)
{
    bool result = true;

    result &= init_vlis();
    result &= test_valid_vli_size();
    result &= test_invalid_vli_size();
    return result ? 0 : 1;
}