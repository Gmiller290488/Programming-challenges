function nbYear(p0, percent, aug, p) {
     var year_count = 0
     while (p0 < p) {
        year_count++;
        p0 = p0+(p0 * (percent/100)) + aug;
     }
     return year_count
     }
