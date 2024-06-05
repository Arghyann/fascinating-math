# fascinating-math

## Newton's fractals.  
Newton's fractals show how numbers in the complex plane behave erratically(kind of like your mom) and small changes in the input spit out dramatically different results. Like if you start with an initial point one millionth of a centimetre away, it tends to a totally different root. It's surreal how chaos comes out of seeminlgy mundane computations.   

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Newton's plan was to approximate the roots of an nth degree polynomial. Remember the quadratic fomula from school? He was trying to do somehthing similar but for a general polynomial. Why approximate, when anything but the exact solution is considered sacrilegious in Mathematics, you ask? Well, this really smart Norweigian guy proved that for any polynomial with a degree greater than four, it is impossible to write a general solution in terms of the functions that we typically use. So, Newton set forth with nothing but the power of Calculus(which he came up with). That's right, he had an idea and he did something about it, because he had a little something of what they call _ambition_. So what have you done with your life?   
   
Newton had no idea about these fractals when he came up with the equation. Like most great things, the nuances only really surfaced after his death. Gives me hope for all the poems I've been working on.   

## Mandelbrot and Julia sets.  
The Mandelbrot and the Julia sets are almost the poster child of math and need no introduction. The fascinating part of the Julia sets is that they predate computers. I can almost imagine nerds painfully checking if a point in space blows up or not on a Saturday night. But luckily for us nerds in the era of computers, we don't have to do that anymore. We can just ask Python to iterate over a million points and it will do it without whining about it. Of course, God forbid you forget a space. Then Python will get mad at you, and I respect that. Setting boundaries is always important.   
$$
z_{n+1} = z_n^2 + c
$$

Both Julia and Mandelbrot sets come from the same equation. Julia sets are obtained by considering a fixed $c$ and letting the initial value of $z$ vary over the plane, whereas Mandelbrot sets have $0$ as the initial value of $z$ and $c$ roams all over the plane. In fact, there exists an entire family of Julia sets for every region in the Mandelbrot set. I highly recommend playing around with this and finding your own cool-looking shapes.   

## The Complex Fourier transform.   
The fourier transform. If I had a penny for everytime I had a sleepless night thinking of why this very code won't work, I'd have two pennies.  

$$
F(\omega) = \int_{0}^{1} f(t) \cdot e^{-i\omega t} \ dt
$$

This seemingly daunting equation produces wonderfully intricate results out of a bunch of rotating vectors. Although very intimidating, [@3b1b](https://github.com/3b1b) has a wonderfully explained video on Youtube about the subject that breaks it down. Infact the inspiration of this whole thing comes from him. 10/10 highly recommend. 

Working with the fourier transform is kind of like contacting your ex again. You'll never know what you're going to get. Sometimes there are these wonderful shapes that make you believe that yes maybe there is a purpose for you, but other times it's just a few jagged lines and a crashed program making you question if it was ever the simple equation you once knew and loved very dearly. 
    
Despite all the pain, suffering and the descent into the deep abyss of nihilism it has caused; the fourier transform is truly a wonderful mathematical tool that can transform a jumbled mess of signals into pure waves. I wish there was a fourier transform for people.
