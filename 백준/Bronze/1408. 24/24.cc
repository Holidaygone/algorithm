#include <stdio.h>

int main(){
    int hour = 0, min = 0, second = 0;
    int ex_hour = 0, ex_min = 0, ex_second = 0;
    int result_h = 0, result_m = 0, result_s = 0;
    scanf("%d:%d:%d", &hour, &min, &second);
    int secondInput = scanf("%d:%d:%d", &ex_hour, &ex_min, &ex_second);
    
    if (secondInput == 3){
        if (ex_second - second >= 0){
            result_s = result_s + ex_second - second;
        }else{
            result_s = result_s + 60 + ex_second - second;
            ex_min -= 1;
        }
        if (ex_min - min >= 0){
            result_m = result_m + ex_min - min;
        }else{
            result_m = result_m + 60 + ex_min - min;
            ex_hour -= 1;
        }
        result_h = result_h + ex_hour - hour;

        // 음수 시간 처리 (24시간 형식 유지)
        if (result_h < 0) {
            result_h += 24;
        }

        printf("%02d:%02d:%02d", result_h, result_m, result_s);
    }else{
        printf("00:00:00");
    }

    return 0;
}