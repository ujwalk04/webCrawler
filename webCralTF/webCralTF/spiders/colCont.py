fore="#f64563"
back="#24D6C7"
mR1=int(fore[1:3],16)
mG1=int(fore[3:5],16)
mB1=int(fore[5:7],16)
mR=mR1/255
mG=mG1/255
mB=mB1/255
if mR<=0.03928:
    R=mR/12.92
else:
    R=((mR+0.055)/1.055)**2.4

if mG<=0.03928:
    G=mG/12.92
else:
    G=((mG+0.055)/1.055)**2.4

if mB<=0.03928:
    B=mB/12.92
else:
    B=((mB+0.055)/1.055)**2.4

lumFG=0.2123*R+0.7152*G+0.0722*B

## background Color

nR1=int(back[1:3],16)
nG1=int(back[3:5],16)
nB1=int(back[5:7],16)
nR=nR1/255
nG=nG1/255
nB=nB1/255
if nR<=0.03928:
    bR=nR/12.92
else:
    bR=((nR+0.055)/1.055)**2.4

if nG<=0.03928:
    bG=nG/12.92
else:
    bG=((nG+0.055)/1.055)**2.4

if nB<=0.03928:
    bB=nB/12.92
else:
    bB=((nB+0.055)/1.055)**2.4

lumBG=0.2123*bR+0.7152*bG+0.0722*bB

##calc
contRat=(lumBG+0.05)/(lumFG+0.05)
print("Calculated Contrast ratio is : "+str('%.2f'%contRat))
print("Since")
if 4.5<=contRat<7:
    print("It is greater than 4.5, It passed the WCAG AA test")
elif contRat>=7:
    print("It is greater than 7, It passed the WCAG AAA test")
else:
    print("It is less than 4.5, It failed the WCAG contrast test ")

