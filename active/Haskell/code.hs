main = do
    putStrLn ""
    getLine >>= readFile >>= putStrLn
    putStrLn ""