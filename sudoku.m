%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% sudoku.m %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% building Aeq matrix for Sudoku Problem

%n=4;  % for 4 by 4 sudoku problem
n=9;  % for 9 by 9 sudoku problem

% x vector (n^3 by 1) contains the decision variables

% Aeq matrix of coefficients for equality constraints
%   There are 4(n^2) + |G| constraints in total.
%   (1) n^2 saying that each column can have only 1 of each integer 1:n
%   (2) n^2 saying that each row can have only 1 of each integer 1:n
%   (3) n^2 saying that each submatrix can have only 1 of each integer 1:n
%   (4) n^2 saying that each element in the matrix must be covered
%   (5) |G| constraints, one for each given element in the initial matrix
%                NOTE: these givens are entered below in "Givens" matrix


Aeq=zeros(4*n^2, n^3);

%% First, fill in Aeq for the n^2 constraints requiring that each column
%%      can have only 1 of each integer 1:n
for i=1:n^2
    Aeq(i,(i-1)*n+1:i*n)=ones(1,n);
end
%% Second, fill in Aeq for the n^2 constraints requiring that each row
%%      can have only 1 of each integer 1:n

for k=1:n
    for i=1:n
        for j=1:n
            Aeq(n^2+i+(k-1)*n,1+(i-1)+(j-1)*n+(k-1)*n^2)=1;
        end
    end
end

%% Third, fill in Aeq for the n^2 constraints requiring that each submatrix
%%      can have only 1 of each integer 1:n

for m=1:sqrt(n)
    for l=1:sqrt(n)
        for j=1:n
            for k=1:sqrt(n)
              Aeq(2*n^2+(m-1)*sqrt(n)*n+(l-1)*n+j,(j-1)*n^2+(l-1)*sqrt(n)+...
                (m-1)*sqrt(n)*n+(k-1)*n+1:...
                (j-1)*n^2+(l-1)*sqrt(n)+(m-1)*sqrt(n)*n+(k-1)*n+sqrt(n))=1;
            end
        end
    end
end

%% Fourth, fill in Aeq for the n^2 constraints requiring that each element 
%%      of the matrix must contain an integer 1:n

for i=1:n
    for j=1:n
        for k=1:n
          Aeq(3*n^2+(i-1)*n+j,(i-1)*n+j + (k-1)*n^2)=1;
        end
    end
end


%% Fifth, if any values of the Sudoku matrix are given, add these as
%%      constraints

% Enter each given value in matrix as triplet (row, col, integer)
% Example for 9-by-9 sudoku
Givens=[1 8 2; 
        2 2 2;
        2 7 5;
        3 3 7;
        3 6 3;
        3 7 4;
        4 1 2;
        4 4 1;
        4 7 3;
        4 8 4;
        5 1 6;
        5 2 4;
        5 5 8;
        5 8 5;
        5 9 9;
        6 2 9;
        6 3 5;
        6 6 2;
        6 9 1;
        7 3 3;
        7 4 4;
        7 7 8;
        8 3 9;
        8 8 1;
        9 2 1];
% turn these given elements into their appropriate position in the x vector
%   of decision variables.
g=size(Givens,1);

for i=1:g
    Aeq(4*n^2+i,Givens(i,1)+(Givens(i,2)-1)*n+(Givens(i,3)-1)*n^2)=1;
end
    


% beq=rhs vector (3n^2 by 1) for equality contraints
beq=ones(4*n^2+g,1);

% run matlab's "bintprog" command
options.MaxRLPIter=500000;
[x,fval,exitflag,output]=bintprog(zeros(n^3,1),[],[],Aeq,beq,[],options);
exitflag
output


% turn matlab's outputed solution vector x into sudoku terms
S=zeros(n,n);
for k=1:n
  subx=find(x((k-1)*n^2+1:k*n^2));
  for j=1:n
      row=mod(subx(j),n);
      if row==0
          row=n;
      end
      S(row,j)=k;
  end
end

% Sudoku Matrix S
S
