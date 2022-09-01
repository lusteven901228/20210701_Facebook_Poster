from upload_files import upload
if __name__ == '__main__':
    print('execute value: range(start, end)')
    x = int(input('start(yy-%%%):'))
    y = int(input('end(yy-%%%):'))
    for i in range(x,y):
        t = upload(i)
        if t:
            print(f'{i} upload failed')
            print(f'Finished posting {i-x} posts in range({x},{i})')
            break
    else:
        print(f"Finished posting {y-x} posts in range({x},{y})")
    input()
