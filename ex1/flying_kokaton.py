import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 押下キーの状態を取得
        key_lst = pg.key.get_pressed()
        
        # 移動量を計算
        dx, dy = -1, 0  # 背景と同じ速度で左に進む
        if key_lst[pg.K_UP]:    # 上矢印キー
            dy -= 1
        if key_lst[pg.K_DOWN]:  # 下矢印キー
            dy += 1
        if key_lst[pg.K_RIGHT]: # 右矢印キー
            dx += 2  # 右方向に進む速度を加える
        
        # こうかとんの移動
        kk_rct.move_ip(dx, dy)

        # 背景描画（ループするスクロール）
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])

        # こうかとんを描画
        screen.blit(kk_img, kk_rct)

        # 画面更新
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
