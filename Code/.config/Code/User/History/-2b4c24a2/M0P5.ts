import { Parser } from 'postcss/lib/postcss'

interface Parse extends Parser {
  default: Parse
}

declare const parse: Parse

export = parse
