from constellationFinder import *

constellation = 'LLLLTSTLLTTLLSLLTSLLSSS'
b=Fraction(0,1)
constant1,constant2 = Threading(constellation)
#[k,n] = findFirstSolution(constant1,constant2)
#Solutions_a0 = [constant1.denominator,n]
#Solutions_an = [constant1.numerator,k]

#print(getFirstNode(Solutions_a0,b,constellation))

print('The equation for the constellation '+constellation+' is a_n = '+str(constant1.print)+' * a_0 + '+str(constant2.print))

#print('The solutions are: a_0 = '+str(Solutions_a0[0])+' * b + '+str(Solutions_a0[1])+', a_n = '+str(Solutions_an[0])+' * b + '+str(int(Solutions_an[1])))

#print('Finally, using b = '+str(b.print)+' we find that one example of this constellation is: '+str(getEachNode(Solutions_a0,b,constellation)))