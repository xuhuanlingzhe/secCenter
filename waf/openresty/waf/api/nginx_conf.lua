local cjson_safe = require "cjson.safe"
local optl = require("optl")

local get_argsByName = optl.get_argsByName
local get_postByName = optl.xget_postByName
local _action = get_argsByName("action")
local _file = get_argsByName("file")
local _data = get_postByName("data")
local sayHtml_ext = optl.sayHtml_ext
local config_dict = ngx.shared.config_dict
local config = cjson_safe.decode(config_dict:get("config")) or {}
local config_base = config.base or {}


function file_exists(name)
	local f = io.open(name, "r")
	if f~=nil then io.close(f) return true else return false end
end
function trim(s)
    return (s:gsub("^%s*(.-)%s*$", "%1"))
end
if _action == "get" then
    local _fp=config_base.baseDir.."conf/vhosts/".._file
    if file_exists(_fp)==false then
        sayHtml_ext({code="error",msg="file not found!",debug=""})
    else
	ngx.log(0,_fp,"")
	local data=optl.readfile(_fp)
	ngx.say(data)
    end
end

if _action == "add" then
    local _fp=config_base.baseDir.."conf/vhosts/".._file
    local _postdata=trim(ngx.decode_base64(_data))
    re = optl.writefile(_fp,_postdata,"w+")
    if not re then
	sayHtml_ext({code="error",msg="file write error!",debug=""})
    else
	sayHtml_ext({code="ok",msg="file write success!",debug=""})
    end
end

if _action == "del" then
    local _fp=config_base.baseDir.."conf/vhosts/".._file
    if file_exists(_fp)==false then
	sayHtml_ext({code="error",msg="file not found!",debug=""})
    else 
	local a=os.remove(_fp)
    	if a~=nil then	
	    sayHtml_ext({code="ok",msg="delete file success!",debug=""})
    	else
            sayHtml_ext({code="error",msg="delete file error,Permission denied!",debug=""})
    	end
    end
end
