import { useContext } from "react"

export const usePathFinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}