'''
begin
assign two set of values as num1 and num2
initializig (num2[0]-num1[0])**0.5 in sum1
initializig (num2[1]-num1[1])**0.5 in sum2
then taking square of sum 1 and sum2 in a variale called distance
print distance
end'''
num1=(45,56)
num2=(65,67)
sum1=(num2[0]-num1[0])**0.5
sum2=(num2[1]-num1[1])**0.5
distance= (sum1+sum2)**2
print(distance)