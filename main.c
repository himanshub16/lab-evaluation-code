#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int check_even(int);

int main()
{
    int test_case_1 = 1;
    int test_case_2 = 4;

    int total_tests = 2;
    int results[] = {
        check_even(test_case_1),
        check_even(test_case_2)
    };

    int answer[] = {
        0,
        1
    };
    int max_score[] = {10, 10};

    int total_score = 0;
    int i;
    for (i = 0; i < total_tests; i++) {
        if (results[i] == answer[i])
            total_score += max_score[i];
    }

    return total_score;
}
