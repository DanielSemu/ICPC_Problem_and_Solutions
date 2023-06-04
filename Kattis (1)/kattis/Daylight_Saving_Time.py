void backward(int d, int h, int m)
{
    int d_h = d / 60;
    int d_m = d % 60;
    h -= d_h;
    m -= d_m;
    if (m < 0)
    {
        h -= 1;
        m += 60;
    }
    if (h < 0)
    {
        h += 24;
    }
    printf("%d %d\n",h,m);
}

def forward(int d, int h, int m)
{
    int d_h = d / 60;
    int d_m = d % 60;
    h += d_h;
    m += d_m;
    if (m >= 60)
    {
        h += 1;
        m -= 60;
    }
    if (h >= 24)
    {
        h -= 24;
    }
    printf("%d %d\n", h, m);
}

def test_case()
{
    char x[2];
    int d,h,m;
    scanf("%s %d %d %d", x, &d, &h, &m);
    if (x[0] == 'F') forward(d,h,m);
    else backward(d,h,m);
}







x=int(input())
for i in range(x):
    y,t,z,p=input().split()
    z=int(z)
    p=int(p)
    t=int(t)
    print(80%60)
    re=0
    if y=='F':
        z=z*60
        res=z+t
        print(res)
        print(res//60 ," " ,res%60)
    elif y=='F':
        print("f")
