from constellationFinder import *

constellation = 'LLLLLTTLLTLSLLSTSTTTSSS'
b=Fraction(3,1)
constant1,constant2 = Threading(constellation)
alpha = constant1.denominator
beta = constant1.numerator
gamma = constant2*constant1.denominator
gdc,x,y = extended_gcd(alpha,beta)

Solutions_a0 = [alpha,gamma*y]
Solutions_an = [beta,gamma*x]

print('The equation for the constellation '+constellation+' is a_n = '+str(constant1.print)+' * a_0 + '+str(constant2.print))

print('The solutions are: a_0 = '+str(Solutions_a0[0].numerator)+'/'+str(Solutions_a0[0].denominator)+' * b + '+str(Solutions_a0[1].numerator)+'/'+str(Solutions_a0[1].denominator)+', a_n = '+str(Solutions_an[0].numerator)+'/'+str(Solutions_an[0].denominator)+' * b + '+str(Solutions_an[1].numerator)+'/'+str(Solutions_an[1].denominator))

print('Finally, using b = '+str(b.print)+' we find that one example of this constellation is: '+str(getEachNode(Solutions_a0,b,constellation)))