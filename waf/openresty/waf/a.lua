function FromBase64(str64)
    local b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    local temp={}
    for i=1,64 do
        temp[string.sub(b64chars,i,i)] = i
    end
    temp['=']=0
    local str=""
    for i=1,#str64,4 do
        if i>#str64 then
            break
        end
        local data = 0
        local str_count=0
        for j=0,3 do
            local str1=string.sub(str64,i+j,i+j)
            if not temp[str1] then
                return
            end
            if temp[str1] < 1 then
                data = data * 64
            else
                data = data * 64 + temp[str1]-1
                str_count = str_count + 1
            end
        end
        for j=16,0,-8 do
            if str_count > 0 then
                str=str..string.char(math.floor(data/math.pow(2,j)))
                data=math.fmod(data,math.pow(2,j))
                str_count = str_count - 1
            end
        end
    end
    local check_last = tonumber(string.byte(str, string.len(str), string.len(str)))  
    if check_last == 0 then  
        str = string.sub(str, 1, string.len(str) - 1)  
    end
    return str
end
local data="IyMjIyMjIyMjIyMjIyMjIyMjIyMgICAgIHdhZiBieSB6aGFuZ2ppZTExICAgICAjIyMjIyMjIyMjIyMjIyMjIw0KDQp1cHN0cmVhbSB3d3dfYmFpZHVfY29tIHsNCiAgICAgICAgaXBfaGFzaDsNCiAgICAgICAgc2VydmVyIDEuMS4xLjEgbWF4X2ZhaWxzPTEgZmFpbF90aW1lb3V0PTEwczsgDQogICAgICAgIHNlcnZlciAyLjIuMi4yIG1heF9mYWlscz0xIGZhaWxfdGltZW91dD0xMHM7IA0KDQogICAgfQ0KDQpzZXJ2ZXIgew0KICAgIGxpc3RlbiAgICAgODA7DQogICAgDQoNCiAgICBzZXJ2ZXJfbmFtZSAgd3d3LmJhaWR1LmNvbTsNCiAgICBpbmRleCBpbmRleC5waHAgaW5kZXguaHRtIGluZGV4Lmh0bWw7DQoNCiAgICANCiAgICBsb2NhdGlvbiB+KiBcLihnaWZ8anBnfHBuZ3xqcGVnfGJtcHxjc3N8anN8Zmx2fGljb3xzd2Z8d29mZikkIHsNCiAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vd3d3X2JhaWR1X2NvbTsNCiAgICAgICAgYWNjZXNzX2xvZyBvZmY7DQogICAgICAgIHByb3h5X3JlZGlyZWN0IG9mZjsNCiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0Ow0KICAgICAgICBwcm94eV9zZXRfaGVhZGVyICAgWC1SZWFsLUlQICAgICAgICAkcmVtb3RlX2FkZHI7DQogICAgICAgICNwcm94eV9zZXRfaGVhZGVyICAgWC1Gb3J3YXJkZWQtRm9yICAkcmVtb3RlX2FkZHI7DQogICAgICAgIHByb3h5X3NldF9oZWFkZXIgICBYLUZvcndhcmRlZC1Gb3IgICRwcm94eV9hZGRfeF9mb3J3YXJkZWRfZm9yOw0KICAgICAgICBwcm94eV9jYWNoZV92YWxpZCAyMDAgMzAyIDZoOw0KICAgICAgICBwcm94eV9jYWNoZV92YWxpZCAzMDEgMWQ7DQogICAgICAgIHByb3h5X2NhY2hlX3ZhbGlkIGFueSAxbTsNCiAgICAgICAgZXhwaXJlcyAzMGQ7DQogICAgICAgIH0NCg0KICAgIGxvY2F0aW9uIC8gew0KICAgICAgICBwcm94eV9wYXNzIGh0dHA6Ly93d3dfYmFpZHVfY29tOw0KICAgICAgICBwcm94eV9zZXRfaGVhZGVyICAgSG9zdCAgICAgICAgICAgICAkaG9zdDsNCiAgICAgICAgcHJveHlfc2V0X2hlYWRlciAgIFgtUmVhbC1JUCAgICAgICAgJHJlbW90ZV9hZGRyOw0KICAgICAgICAjcHJveHlfc2V0X2hlYWRlciAgIFgtRm9yd2FyZGVkLUZvciAgJHJlbW90ZV9hZGRyOw0KICAgICAgICBwcm94eV9zZXRfaGVhZGVyICAgWC1Gb3J3YXJkZWQtRm9yICAkcHJveHlfYWRkX3hfZm9yd2FyZGVkX2ZvcjsNCiAgICAgICAgfQ0KICAgIGFjY2Vzc19sb2cgIGxvZ3Mvd3d3LmJhaWR1LmNvbS5hY2Nlc3MubG9nIG1haW47DQogICAgZXJyb3JfbG9nICBsb2dzL3d3dy5iYWlkdS5jb20uZXJyb3IubG9nIDsNCn0NCg=="
local a= FromBase64(data)
print(a)
