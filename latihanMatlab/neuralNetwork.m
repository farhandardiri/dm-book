function xnew=scale(x,BB,BA)
[Xmax]=max(x);
[Xmin]=min(x);
[R,C]= size(x);
xnew=(x-ones(R,1)*Xmin).*(ones(R,1)*((BA-BB)*ones(1,C)./(Xmax-Xmin)))+BB;