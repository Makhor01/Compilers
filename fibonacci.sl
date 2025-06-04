n = 10;
a = 0;
b = 1;
i = 1;

while (i < n) {
    temp = a + b;
    a = b;
    b = temp;
    i = i + 1;
}

print b;