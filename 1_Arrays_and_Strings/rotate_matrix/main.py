"""
- Rotate Matrix: Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes,
 write a method to rotate the image by 90 degrees. Can you do this in place? 

**!!! Ta errado nao sei pq**
"""

def rotate90deg(mtx, N):
    temp = [[1]*N]*N
    print(temp)
    print(mtx)

    for a in range(N):
        d = N - 1 - a
        for b in range(N):
            c = b
            temp[c][d] = mtx[a][b]
            print(f"{a}x{b} -> {c}x{d} = {mtx[a][b]}")
            print(temp)

        print(temp)
    return temp

print(rotate90deg([ [1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]], 3))