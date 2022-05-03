#include <stdio.h>
#include <vesa.h>

#define DIRECTION_LEFT  0
#define DIRECTION_UP    1
#define DIRECTION_RIGHT 2
#define DIRECTION_DOWN  3

int main(){
    int SIZE_SNAKE = 1;     // изначальный размер змейки
    int X_SNAKE = 150;      // координат X змейки, изначально по центру
    int Y_SNAKE = 150;      // координат Y змейки, изначально по центру
    int RUN_GAME = 1;       // для запуска игры 1, для остановки 0
    int DIRECTION = 0;       // направление змейки

    while(RUN_GAME){
        draw_field();
        draw_snake(X_SNAKE, Y_SNAKE);
        if(Y_SNAKE == 0 || Y_SNAKE == 300 || X_SNAKE == 0 || X_SNAKE == 300) RUN_GAME = 0;
        switch(DIRECTION){
            case DIRECTION_LEFT:
                X_SNAKE -= 10;
                break;
            case DIRECTION_UP:
                Y_SNAKE -= 10;
                break;
            case DIRECTION_RIGHT:
                X_SNAKE += 10;
                break;
            case DIRECTION_DOWN:
                Y_SNAKE += 10;
                break;
        }
        if(keyboard_map[getscancode()] == 'w') DIRECTION = DIRECTION_UP;
        if(keyboard_map[getscancode()] == 'a') DIRECTION = DIRECTION_LEFT;
        if(keyboard_map[getscancode()] == 's') DIRECTION = DIRECTION_DOWN;
        if(keyboard_map[getscancode()] == 'd') DIRECTION = DIRECTION_RIGHT;
    }
    return 0;
}

void draw_snake(int X, int Y){
    for(int i=1; i<11; i++)
            for(int j=1; j<11; j++)
                draw_pixel(X+i, Y+j, VESA_BLACK);
}

void draw_field(){
    /* Вырисовываем игровое поле 300x300 */
    for(int i=0; i<300; i++)
        for(int j=0; j<300; j++)
            draw_pixel(i, j, VESA_BLUE);
}