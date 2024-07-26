import { Stringifier } from 'postcss/lib/postcss'

interface Stringify extends Stringifier {
  default: Stringify
}

declare const stringify: Stringify

export = stringify
