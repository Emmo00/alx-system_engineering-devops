#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:(?<SENDER>.+)\]\s\[to:(?<RECEIVER>.+)\]\s\[flags:(?<FLAGS>.+)\])\s\[msg:/).join(",")
