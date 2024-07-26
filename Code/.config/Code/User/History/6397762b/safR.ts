import { JSONHydrator } from 'postcss/lib/postcss'

interface FromJSON extends JSONHydrator {
  default: FromJSON
}

declare const fromJSON: FromJSON

export = fromJSON
