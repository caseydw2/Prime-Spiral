# Prime Spiral
`draw_spiral` creates a spiral of increasing integers, starting with 1 in the middle of the spiral. Natural numbers that are prime produce a white disc over their place in the spiral. This is what is known as an "Ulam spiral", or more colloquially a "Prime Sprial". More information on the spiral can be found on [its wikipedia page](https://en.wikipedia.org/wiki/Ulam_spiral).

Inspiration of this project came from [this Numberphile video](https://youtu.be/iFuR97YcSLM). 

The spiral has the interesting property that the distribution of primes seem non-random. There are diagonal lines spread out through the spiral as the size of the spiral gets bigger. 
![Prime Spiral sprl_num 300, factor 50](https://user-images.githubusercontent.com/74943315/155056649-993b3068-117b-43ea-9e21-b9a98f977415.png)


`polar_prime_plot` cycles through integers up to 10<sup>ten_pwr</sup>. For each prime number, p, we draw a circle at the polar coordinates (p,p). The spiral below is when ten_pwr = 4
![polar prime plot ten_pwr 4, factor 10](https://user-images.githubusercontent.com/74943315/155235031-0ca41e1d-b55a-4aa3-b7ab-21064e22899f.png)

As usual, a math channel on youtube inspired me to create my own prime spiral. This [video](https://youtu.be/EK32jo7i5LQ) was created by 3Blue1Brown. 
