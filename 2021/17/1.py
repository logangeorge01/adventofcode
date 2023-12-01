


x = (265, 287)
y = (-103, -58)

ans = -10000
for i in range(100):
   for j in range(1000):
      vx, vy = i, j
      px, py = 0, 0
      my = -10000

      while True:
         if x[0] <= px <= x[1] and y[0] <= py <= y[1]:
            ans = max(ans, my)
            break
         px += vx
         py += vy
         my = max(my, py)
         if px > x[1] or py < y[0]:
            break
         if vx < 0: vx += 1
         elif vx > 0: vx -= 1
         vy -= 1

print(ans)




