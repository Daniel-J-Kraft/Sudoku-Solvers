clear;
tic
error_count = 0;
cvx_begin
    variable x(9,9,9)
    minimize sum(sum(sum(abs(x))))
    subject to
        sum(x,1)==1;%Rows sum
        sum(x,2)==1;
        sum(x,3)==1;
        sum(sum(x(1:3,1:3,:)))==1;
        sum(sum(x(1:3,4:6,:)))==1;
        sum(sum(x(1:3,7:9,:)))==1;
        sum(sum(x(4:6,1:3,:)))==1;
        sum(sum(x(4:6,4:6,:)))==1;
        sum(sum(x(4:6,7:9,:)))==1;
        sum(sum(x(7:9,1:3,:)))==1;
        sum(sum(x(7:9,4:6,:)))==1;
        sum(sum(x(7:9,7:9,:)))==1;
        %x(1,1,5)==1; %Initialization Constraints
        %x(1,2,3)==1;
        %x(1,5,7)==1;
        %x(2,1,6)==1;
        %x(2,4,1)==1;
        x(2,5,9)==1;
        x(2,6,5)==1;
        x(3,2,9)==1;
        x(3,3,8)==1;
        x(3,8,6)==1;
        x(4,1,8)==1;
        x(4,5,6)==1;
        x(4,9,3)==1;
        x(5,1,4)==1;
        x(5,4,8)==1;
        x(5,6,3)==1;
        x(5,9,1)==1;
        x(6,1,7)==1;
        x(6,5,2)==1;
        x(6,9,6)==1;
        x(7,2,6)==1;
        x(7,7,2)==1;
        x(7,8,8)==1;
        x(8,4,4)==1;
        x(8,5,1)==1;
        x(8,6,9)==1;
        x(8,9,5)==1;
        x(9,5,8)==1;
        x(9,8,7)==1;
        x(9,9,9)==1;
        cvx_end
        x=round(x);
        result=zeros(9,9);
        
        for i=1:9
            for j=1:9
                if sum(x(i,j,:)) == 1
                    k=find(x(i,j,:));
                    result(i,j)=k;
                else
                    error_count = error_count +1
                    result(i,j)=0;
                end
            end
        end

% show the results
result
toc