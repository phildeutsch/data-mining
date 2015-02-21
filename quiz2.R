chi = function(x) {
    total_a = c(x[1] + x[2], x[3] + x[4])
    total_b = c(x[1] + x[3], x[2] + x[4])

    e = c(  total_b[1] * total_a[1] / sum(total_a), 
            total_a[1] * total_b[1] / sum(total_a), 
            total_b[2] * total_a[2] / sum(total_a), 
            total_a[2] * total_b[2] / sum(total_a) 
         )
    print(sum((e-x)^2/e))
}
