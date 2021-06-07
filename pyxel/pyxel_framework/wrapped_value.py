class WrappedValue:
    def __init__(self, v):
        if callable(v):
            self.func = v
        else:
            def inner():
                return (v)
            self.func = inner
    
    def __call__(self):
        return self.func()

if __name__ == "__main__":
    def return_100():
        return (100)
    
    wv = WrappedValue(20)
    wv_func = return_100

    print(wv())
    print(wv_func())