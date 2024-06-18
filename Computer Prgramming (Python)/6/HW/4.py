def money(x):
    x1000 = x // 1000
    x500  = (x % 1000) // 500
    x100  = (x % 500) // 100
    x50   = (x % 100) // 50
    x20   = (x % 50) // 20 
    x10   = (x % 20) // 10  
    x5    = (x % 10) // 5
    x2    = (x % 5) // 2
    x1    = x % 2

    return [x1000, x500, x100, x50, x20, x10, x5, x2, x1]

outing = money(1693)
print("1000-Baht notes:", outing[0], "\n",
      "500-Baht notes:", outing[1], "\n",
      "100-Baht notes:", outing[2], "\n",
      "50-Baht notes:", outing[3], "\n",
      "20-Baht notes:", outing[4], "\n",
      "10-Baht coins:", outing[5], "\n",
      "5-Baht coins:", outing[6], "\n",
      "2-Baht coins:", outing[7], "\n",
      "1-Baht coins:", outing[8], "\n")
