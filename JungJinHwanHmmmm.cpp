#include <stdio.h>

int main(void)
{
	int num, sum = 0;

	while (1)
	{
		print("정수를 입력하세요 : ");
		scanf("%d", &num);
		sum += num;					//여기가 더하는 거임
		if (num == 0)
		{
			printf("합계 : %d", sum);
			break;
		}
	}
}