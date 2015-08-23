from tkinter import *
from PIL import Image, ImageTk

weights = [
    [
        [2.6311821237398259, -2.0345086491295068, -3.1103584534113589, 3.851457752828185, -1.2084739835943772, -5.4294283102403815, -5.201566341582069, -0.72124596658278983, -2.3164752826130353, -1.1192867104971636, -3.5063406378887634, 1.0786866127978296, -0.15180892326212364],
        [3.8197323528142451, -2.2126692299092392, 4.9904993748826856, -6.0639585826731022, 2.5332073282360805, 1.822074924164653, -5.9286029992992919, 0.58215121976400064, -1.054455672007903, -1.2606800615087348, 5.5749356981210836, 0.10712194032396526, 1.0523400946152426],
        [-5.1241951590756747, -1.6172446913094403, -3.3558943806430785, 4.0326911600941306, -1.8713691911846781, 1.4266149241739741, 8.5531599492383776, -0.74582984959057419, -1.2638194124382001, -1.5043393662413878, -3.7200468613571687, -0.66202088427842776, -1.9834979435690774],
        [2.5918260983101979, -2.0414544088634625, -3.0795793901621149, 3.8492056953491227, -0.91779301318388617, -5.4036237866626236, -5.167591601835789, 0.58936426345883175, -2.4264003607176456, -1.4801045167865363, -3.5132800789864862, -1.9400336170825372, 1.0028754558322861]
    ]
    ,[
        [-4.7017417121953109],
        [-5.5693787810501849],
        [5.2932463848676266],
        [-6.2297032439479834],
        [1.936901353660196],
        [-15.696822468344434],
        [13.355131871809837],
        [0.57555940255154092],
        [-4.3984485527473041],
        [-2.532719868645851],
        [6.3909247115374823],
        [0.47690476034658519],
        [-0.3335800218652078]
    ]
]

# Some constants you may want to change
win_height = 700
win_width = 700
node_radius = 10

win = Tk()
win.title("NetVis - Neural Network visualisation")

# création des widgets "enfants" :
can1 = Canvas(win,bg='dark grey',height=win_height, width=win_width)
can1.pack()

def draw_weights(canvas, nodes_a, nodes_b, weights, abs_max):
    for (i, m) in enumerate(weights):
        for (j, _) in enumerate(weights[i]):
            (start_x, start_y) = nodes_a[i]
            (end_x, end_y) = nodes_b[j]
            val = 255 * abs(weights[i][j])/abs_max
            width = int(val/15)
            rgb = (1*int(val), 0, 0) if weights[i][j]>0 else (0, 1*int(val), 0)
            color = '#%02x%02x%02x' % rgb  # set your favourite rgb color
            canvas.create_line(start_x, start_y, end_x, end_y, width=width, fill=color)



# positionning nodes ...
node_pos = []

# ... input and intermediate nodes
dx_node = win_height/(len(weights)+2)
for (n, s) in enumerate(weights):
    node_pos.append([])
    x_node = (n+1) * dx_node
    num_node = len(weights[n])
    dy_node = win_height/(num_node+1)
    for i in range(num_node):
        y_node = (i+1) * dy_node
        node_pos[n].append((x_node, y_node))

# ... output
x_node = win_height - dx_node
y_node = win_height/2
node_pos.append([(x_node, y_node)])


# drawing on canvas ...
# ... arc
for (n, s) in enumerate(weights):
    vals = [i for j in weights[n] for i in j]
    max_val = max(vals)
    min_val = min(vals)
    abs_max = max_val if max_val>-min_val else -min_val
    draw_weights(can1, node_pos[n], node_pos[n+1], weights[n], abs_max)

# ... nodes
for l in node_pos:
    for pos in l:
        can1.create_oval(pos[0]-node_radius, pos[1]-node_radius, pos[0]+node_radius, pos[1]+node_radius, width=2, fill='red')

win.mainloop()
