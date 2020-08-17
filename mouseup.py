import pyautogui as pg
import multiprocessing
import time
print(pg.position())
def foo():
   pg.moveTo(427,356)
   pg.mouseDown(button='left')  # press the left button down
if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo)
    p.start()
    # Wait 69 seconds for foo
    time.sleep(6)
    pg.mouseUp(button='left', x=427, y=356)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()