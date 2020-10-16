function [binMat] = SudokuConv(G)
    binMat = zeros(9,9,9)
    for i = 1:9
        for j = 1:9
            k = G(i,j);
            binMat(i,j,k) = 1;
        end
    end
end
           