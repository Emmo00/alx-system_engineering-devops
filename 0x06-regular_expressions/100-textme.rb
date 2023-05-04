#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:(?<SENDER>\w+)\]\s\[to:(?<RECEIVER>.+)[0-9]\]\s\[flags:(?<FLAGS>.+)\])\s\[msg:/).join(",")
