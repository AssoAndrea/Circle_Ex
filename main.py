import graph

if __name__ == '__main__':
    c1 = graph.MyCircle(1, 1, 0.2,color="blue")
    c2 = graph.MyCircle(0.1, 2, 0.4,color="violet")
    c3 = c1 + c2
    print(c3>c1)
    print(c3==c1)
    c4 = graph.MyCircle(0.4, 0.6, 3, color="green")

    graph.add_circle(c1)
    graph.add_circle(c2)
    graph.add_circle(c3)
    graph.add_circle(c4)
    graph.sort_circles()
    graph.draw_figure()
