colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

for i in range(500):
  t.forward(i)
  t.color(colors[i % len(colors)])
  t.left(500)
